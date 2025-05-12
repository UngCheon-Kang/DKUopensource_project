from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Review
from .forms import ReviewForm
from search.models import OTCMedicine

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(OTCMedicine, id=medicine_id)
    reviews = Review.objects.filter(medicine=medicine)
    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0

    context = {
        'medicine': medicine,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),
    }
    return render(request, 'detail/medicine_detail.html', context)

@login_required
def add_review(request, medicine_id):
    medicine = get_object_or_404(OTCMedicine, id=medicine_id)
    review = Review.objects.filter(user=request.user, medicine=medicine).first()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.user = request.user
            updated.medicine = medicine
            updated.save()
            return redirect('detail:medicine_detail', medicine_id=medicine.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'detail/add_review.html', {
        'form': form,
        'medicine': medicine,
        'is_edit': bool(review),  # 템플릿에서 '수정' 여부 판단용
    })

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SkateTrick, TrickCategory, UserProgress

def landing_page(request):
    """Display the landing page."""
    return render(request, 'skate_trick_index/landing.html')

def trick_list(request):
    """Display all skate tricks with filtering options."""
    tricks = SkateTrick.objects.all()
    categories = TrickCategory.objects.all()
    
    # Filter by category if specified
    category_id = request.GET.get('category')
    if category_id:
        tricks = tricks.filter(category_id=category_id)
    
    # Filter by difficulty if specified
    difficulty = request.GET.get('difficulty')
    if difficulty:
        tricks = tricks.filter(difficulty=difficulty)
    
    context = {
        'tricks': tricks,
        'categories': categories,
    }
    return render(request, 'skate_trick_index/trick_list.html', context)

def trick_detail(request, trick_id):
    """Display detailed information about a specific trick."""
    trick = get_object_or_404(SkateTrick, id=trick_id)
    user_progress = None
    
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(
            user=request.user,
            trick=trick
        ).first()
    
    context = {
        'trick': trick,
        'user_progress': user_progress,
    }
    return render(request, 'skate_trick_index/trick_detail.html', context)

@login_required
def update_progress(request, trick_id):
    """Update user's progress on a specific trick."""
    trick = get_object_or_404(SkateTrick, id=trick_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        notes = request.POST.get('notes', '')
        
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            trick=trick,
            defaults={'status': status, 'notes': notes}
        )
        
        if not created:
            progress.status = status
            progress.notes = notes
            progress.save()
        
        messages.success(request, f'Progress updated for {trick.name}!')
        return redirect('trick_detail', trick_id=trick.id)
    
    return redirect('trick_detail', trick_id=trick.id) 
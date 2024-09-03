<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SearchIndex extends Model
{
    use HasFactory;
    protected $table = 'search_indices';
    protected $fillable = ['query', 'url', 'language', 'country', 'page_limiter', 'keywords', 'index', 'timer'];
}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SeoTestMetaDescription extends Model
{
    use HasFactory;

    protected $fillable = [
        'url', 'scraper_id', 'scraped_url_id',
        'description',
        'is_satisfied',
        'weight',
        'description_length',
        'suggestion',
    ];
}
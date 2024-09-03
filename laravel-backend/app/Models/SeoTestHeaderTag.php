<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SeoTestHeaderTag extends Model
{
    use HasFactory;

    protected $table = 'seo_test_header_tags';

    protected $fillable = [
        'url', 'scraper_id', 'scraped_url_id',
        'is_satisfied',
        'is_h2_satisfied',
        'weight',
        'headers',
        'suggestion',
        'keyword_count_outside_h1'
    ];
}
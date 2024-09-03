<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SeoTestKeywordOptimization extends Model
{
    protected $table = 'seo_test_keyword_optimizations';

    protected $fillable = [
        'url', 'scraper_id', 'scraped_url_id',
        'is_primary_satisfied',
        'is_secondary_satisfied',
        'primary_keyword',
        'weight',
        'suggestion',
    ];
}
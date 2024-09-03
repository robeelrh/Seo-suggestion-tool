<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SeoTestFavicon extends Model
{
    use HasFactory;
    protected $table = 'seo_test_favicons';
    protected $fillable = ['url', 'scraper_id', 'scraped_url_id', 'link', 'is_satisfied' ,'suggestion', 'weight'];
}
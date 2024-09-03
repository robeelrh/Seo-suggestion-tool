<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SeoTestDocType extends Model
{
    use HasFactory;
    protected $table = 'seo_test_doc_type';
    protected $fillable = ['url', 'scraper_id', 'scraped_url_id', 'is_satisfied','suggestion', 'weight'];
}
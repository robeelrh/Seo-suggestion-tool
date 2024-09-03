<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SeoTestTitleTag extends Model
{
    use HasFactory;
    protected $fillable = ['url', 'scraper_id', 'scraped_url_id', 'title', 'is_satisfied', 'weight', 'title_len','suggestion',];
}
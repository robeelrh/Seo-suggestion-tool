<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ScrapedImage extends Model
{
    use HasFactory;
    protected $table = 'scraped_images';
    protected $fillable = ['scraped_url_id', 's3_url' ];
}

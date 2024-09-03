<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Scraper extends Model
{
    use HasFactory;
    protected $table = 'scrapers';
    protected $fillable = [ 
        'scraper_id', 
        'project_id', 
        'domain_url', 
        'trace_able', 
        'follow_links',
        'sleep_time',
        'status',
        'started_at',
        'ended_at',
        'follow_index',
        'follow_noindex',
        'nofollow_index',
        'nofollow_noindex',
        'no_meta_no_robots' 
    ];

    public function scrapedUrls()
    {
        return $this->hasMany(ScrapedUrls::class, 'scraper_id', 'id');
    }
}

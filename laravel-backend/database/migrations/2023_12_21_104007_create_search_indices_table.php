<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('search_indices', function (Blueprint $table) {
            $table->id();
            $table->string('query')->nullable();
            $table->string('url')->nullable();
            $table->string('language')->nullable();
            $table->string('country')->nullable();
            $table->string('page_limiter')->nullable();
            $table->string('keywords')->nullable();
            $table->string('index')->nullable();
            $table->string('timer')->nullable();
            $table->unsignedBigInteger('scraper_id');
            $table->unsignedBigInteger('url_id')->nullable();
            $table->foreign('scraper_id')->references('id')->on('scrapers');
            $table->foreign('url_id')->references('id')->on('scraped_urls');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('search_indices');
    }
};

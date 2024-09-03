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
        Schema::create('seo_test_iframes_counts', function (Blueprint $table) {
            $table->id();

            $table->string('url')->nullable();
            $table->integer('scraper_id')->default(0);
            $table->integer('scraped_url_id')->default(0);

            $table->boolean('is_satisfied')->default(true);
            $table->integer('iframes_count')->default(0);
            $table->integer('weight')->default(0);
            $table->string('suggestion')->nullable();

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('seo_test_iframes_counts');
    }
};

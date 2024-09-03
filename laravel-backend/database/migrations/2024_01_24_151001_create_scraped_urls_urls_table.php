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
        Schema::create('scraped_urls_urls', function (Blueprint $table) {

            $table->id();
            $table->timestamps();

            $table->string('url');
            $table->unsignedBigInteger('scraped_url_id')->nullable();
            $table->foreign('scraped_url_id')->references('id')->on('scraped_urls');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('scraped_urls_urls');
    }
};

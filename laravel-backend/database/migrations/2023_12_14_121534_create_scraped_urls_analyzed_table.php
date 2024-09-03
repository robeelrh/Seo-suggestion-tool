<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('scraped_urls_analyzed', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('scraped_url_id');
            $table->unsignedBigInteger('page_speed');
            $table->string('file_size');
            $table->string('breadcrumb');
            $table->float('content_percentage');
            $table->float('primary_key_percentage');
            $table->string('ssl_protocol');
            $table->string('valid_till');
            $table->string('new_protocol_version');
            $table->foreign('scraped_url_id')->references('id')->on('scraped_urls');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('scraped_urls_analyzed');
    }
};

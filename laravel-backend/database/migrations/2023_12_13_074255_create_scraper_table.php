<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('scrapers', function (Blueprint $table) {
            $table->id();
            $table->string('scraper_id')->nullable();
            $table->string('project_id')->nullable();
            $table->string('domain_url')->nullable();
            $table->string('trace_able')->nullable();

            $table->string('status')->nullable();
            $table->string('ended_at')->nullable();
            $table->string('started_at')->nullable();

            $table->string('follow_links')->nullable();
            $table->string('sleep_time')->nullable();

            $table->unsignedInteger('follow_index')->default(0);
            $table->unsignedInteger('follow_noindex')->default(0);
            $table->unsignedInteger('nofollow_index')->default(0);
            $table->unsignedInteger('nofollow_noindex')->default(0);
            $table->unsignedInteger('no_meta_no_robots')->default(0);

            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('scrapers');
    }
};
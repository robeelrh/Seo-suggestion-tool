<?php

namespace App\Http\Controllers;

use App\Models\Scraper;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class ScraperGetAllByProjectController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'project_id' => 'required',
        ]);
        $scraper = Scraper::where([
            ['project_id', '=', $request->get('project_id')]
        ])->get();

        if (empty($scraper)) {
            return response()->json([
                'errors' => [
                    'scraper' => 'The scraper does not exist',
                ]
            ], 422);
        }
        return response()->json($scraper);
    }
}

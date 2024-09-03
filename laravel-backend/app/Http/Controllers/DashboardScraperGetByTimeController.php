<?php


namespace App\Http\Controllers;
use App\Models\Scraper;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class DashboardScraperGetByTimeController extends Controller
{
    public function handle(Request $request){
        
        $this->validate($request, [
            'project_id' => 'required',
            'start_date' => 'required|date_format:Y-m-d',
            'end_date' => 'required|date_format:Y-m-d'
        ]);
        $startDate = $request->input('start_date');
        $endDate = $request->input('end_date');
        $scrapers = Scraper::where('project_id', $request->input('project_id'))
            ->whereDate(\DB::raw('DATE(created_at)'), '>=', $startDate)
            ->whereDate(\DB::raw('DATE(created_at)'),'<=',$endDate)
            ->get();

        return response()->json(
            $scrapers
        );
    }
}
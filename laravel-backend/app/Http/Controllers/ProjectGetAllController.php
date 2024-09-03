<?php

namespace App\Http\Controllers;

use App\Models\Project;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ProjectGetAllController extends Controller
{
    public function handle()
    {
        $projects = Project::get();
        if (empty($projects)) {
            return response()->json([
                'errors' => [
                    'projects' => 'The projects does not exist',
                ]
            ], 422);
        }
        return response()->json([
            'success'=>[
                'projects'=> 'Projects fetched successfully'
            ],
            'projects'=> $projects
        
        ],200);
    }
}

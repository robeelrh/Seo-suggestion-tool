<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use App\Models\ScrapedImage;

class ImageUploadController extends Controller
{
    public function handle(Request $request)
    {
        // Validate the request...
        $request->validate([
            'image' => 'required|image|mimes:jpeg,png,jpg,gif,svg|max:2048',
        ]);

        // Upload the image to S3...
        $image = $request->file('image');
        $imageName = pathinfo($image->getClientOriginalName(), PATHINFO_FILENAME);
        $imageName = $imageName . '_' . time() . '.' . $image->extension();
        $path = Storage::disk('s3')->put($imageName, file_get_contents($image), 'public');

        // Get the URL of the uploaded image...
        $url = Storage::disk('s3')->url($imageName);

        // Save the URL to the database...
        $imageModel = new ScrapedImage;
        $imageModel->scraped_url_id = $request->scraped_url_id;
        $imageModel->s3_url = $url;
        $imageModel->save();

        return response()->json($imageModel, 201);
    }
}
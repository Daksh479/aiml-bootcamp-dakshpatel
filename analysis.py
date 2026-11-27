# • Generate a dataset: 100 students × 5 exams of random marks between 30 and 100. Seed your generator so
#   results are reproducible.
# • Compute each student's average and each exam's average. State which axis you used for each.
# • Find how many students passed (average ≥ 60), and what fraction that is.
# • Find the top 10 students by average — return their indices and their scores.
# • Standardise the marks per exam (mean 0, std 1), so exams of different difficulty become comparable.
# • Apply a curve: add 5 marks to everyone but cap at 100. Report how many marks hit the cap.
# • Identify any student who failed every single exam. (Hint: a mask, then an all-along-an-axis check.)
# • Do all of it without a single Python loop.

import numpy as np

# 1. Dataset: 100 students x 5 exams, integer marks 30-100, seeded
rng = np.random.default_rng(42)
marks = rng.integers(30, 101, size=(100, 5))   # high is exclusive, so 101

# 2. Averages
student_avg = marks.mean(axis=1)   
exam_avg    = marks.mean(axis=0)   

# 3. Pass count and fraction (average >= 60)
passed = student_avg >= 60         
n_passed = passed.sum()            
frac_passed = passed.mean()        

# 4. Top 10 students by average
order = np.argsort(student_avg)[::-1]      
top10_idx = order[:10]
top10_scores = student_avg[top10_idx]

# 5. Standardise per exam (z-scores): (x - mean) / std, down each column
z = (marks - marks.mean(axis=0)) / marks.std(axis=0)

# 6. Curve: +5, cap at 100
curved_raw = marks + 5
n_capped = (curved_raw > 100).sum()       
curved = np.minimum(curved_raw, 100)    

# 7. Students who failed every exam (mark < 60 in all 5)
failed_all = (marks < 60).all(axis=1)     
failed_all_idx = np.where(failed_all)[0]

print("Student averages (first 5):", student_avg[:5].round(2))
print("Exam averages (axis=0):    ", exam_avg.round(2))
print(f"Passed: {n_passed} of {len(marks)} ({frac_passed:.0%})")
print("Top 10 indices:", top10_idx)
print("Top 10 scores: ", top10_scores.round(2))
print("Z-score check -> column means:", z.mean(axis=0).round(6), " stds:", z.std(axis=0).round(6))
print("Marks hitting the cap after +5:", n_capped, "| max after curve:", curved.max())
print("Failed every exam (indices):", failed_all_idx)
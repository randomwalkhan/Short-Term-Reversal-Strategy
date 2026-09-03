# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 10:15:01 EDT`
Last processed slot: `early_entry_1015`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$74,478.10`
- Equity: `$74,478.10`
- Realized PnL: `$64,478.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CPRT     option         option CPRT261016C00032500    144          2026-09-01         2026-09-03        1.650       2.800 16560.0   69.696970 take_profit_day2_hit_at_scan
  MSTR     option         option MSTR261009C00122000     20          2026-09-02         2026-09-03       11.475      16.575 10200.0   44.444444 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  REGN          100.00               20            1.09              6.52        849.23                27.66         0.538            pass              0.520              0.0                           0.174                1.94              0.050                                 ok            True                  False
  CSCO           84.62               26            1.22              0.93        109.06                36.36         0.533            pass              0.368             28.3                           0.304               -1.34             -0.155                                 ok            True                  False
 CMCSA           92.31               26            0.69              0.13         26.75                26.14         0.516            pass              0.486              0.0                           0.013                0.78             -0.081                                 ok            True                  False
  AMGN           96.30               27            0.52              1.61        442.15                21.97         0.508            pass              0.719             51.6                           0.421                2.16              0.023                                 ok            True                  False
  CHTR           83.33               12            3.52              3.92        157.29                59.56         0.500            pass              0.170              5.9                           0.097                3.80              0.267                                 ok            True                  False
  MRVL           81.58               38            0.11              0.16        206.41                78.54         0.656            pass              0.582             95.8                           0.675              -17.83             -1.973 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00               33            0.73              0.28         54.55                55.99         0.596            pass              0.613              0.0                           0.150              -12.89             -1.936 downtrend_blocked_slope_and_streak           False                  False
  SBUX           88.89                9            1.35              1.01        106.29                21.58         0.556            pass              0.293              0.0                           0.150                1.24              0.013                                 ok           False                  False
  MCHP           86.96               23            2.25              1.15         72.27                58.99         0.547            pass              0.414             29.0                           0.182               -5.62             -0.523            downtrend_blocked_slope           False                  False
  PANW           87.23               47            0.13              0.31        328.35                70.92         0.520            pass              0.726             93.8                           0.873               -6.16             -0.219                                 ok           False                  False
  DRAM           83.33               30            2.54              1.00         55.78                63.42         0.509            pass              0.351             26.0                           0.278               -4.85             -0.269            downtrend_blocked_slope           False                  False
   CSX           90.00               20            0.52              0.18         48.57                16.27         0.494 below_threshold              0.536             51.0                           0.261               -4.79             -0.608 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-09-03T10:15:01.925464-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.51, "early_entry_score": 0.76, "early_reclaim_pct": 75.0, "entry_ask": 7.7, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 37239.05, "hypothetical_contracts": 54, "matched_signals": 44, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 71.0, "option_spread_pct": 24.82, "option_volume": 57.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.781, "shadow_only": true, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.76, "early_reclaim_pct": 75.0, "matched_signals": 44, "recovery_stability_score": 0.781, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:10:01.856721-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:05:01.913040-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:00:03.820107-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T09:50:05.699524-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"asset_type": "option", "contract_symbol": "MSTR261009C00122000", "fill_price": 16.575, "pnl": 10200.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 44.44, "ticker": "MSTR"}
2026-09-03T09:50:05.699524-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "CPRT261016C00032500", "fill_price": 2.8, "pnl": 16560.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 69.7, "ticker": "CPRT"}
2026-09-03T00:00:02.675455-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 93}
2026-09-02T15:10:01.537083-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-02T15:05:01.526637-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-02T15:00:06.384646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903101501)

</details>

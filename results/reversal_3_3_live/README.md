# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 11:10:06 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$142,574.30`
- Equity: `$142,574.30`
- Realized PnL: `$132,574.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0   27.397260 take_profit_day2_hit_at_scan
   CEG     option         option  CEG261120C00290000     31          2026-10-12         2026-10-13        18.65       21.65  9300.0   16.085791 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           88.24               17            0.94              0.76        115.02                34.19         0.562            pass              0.497             58.1                           0.362                7.26              0.905                                 ok            True                  False
  MDLZ           93.75               16            0.68              0.29         61.66                19.83         0.553            pass              0.543             27.0                           0.379                4.37              0.648                                 ok            True                  False
  UPRO           83.87               31            0.54              0.59        155.21                28.94         0.521            pass              0.330             11.6                           0.147                4.50              0.582                                 ok            True                  False
  SHOP           84.62               39            0.60              0.76        178.90                48.43         0.507            pass              0.607             80.0                           0.652               20.15              2.079                                 ok            True                  False
  SNPS           76.47               17            1.67              5.87        500.00                52.43         0.587            pass              0.217             37.2                           0.281               19.04              1.478                                 ok           False                  False
  INTC           88.57               35            1.28              0.91        100.96                67.41         0.562            pass              0.627             58.4                           0.471              -13.70             -1.884 downtrend_blocked_slope_and_streak           False                  False
  MPWR           82.35               17            2.34             21.64       1309.96                51.39         0.541            pass              0.199             11.8                           0.159               -4.85             -0.376            downtrend_blocked_slope           False                  False
   KDP           96.77               31            0.03              0.01         32.75                30.00         0.540            pass              0.882             96.2                           0.744                5.51              0.657                                 ok           False                  False
  MCHP           95.45               22            1.59              0.82         73.48                37.42         0.502            pass              0.638             35.8                           0.245               -7.77             -0.836            downtrend_blocked_slope           False                  False
   STX           85.00               20            3.37             17.76        745.64                70.16         0.501            pass              0.433             61.1                           0.571              -20.32             -2.535            downtrend_blocked_slope           False                  False
  NVDA           87.50               24            0.70              1.11        225.85                22.13         0.491 below_threshold              0.497             51.5                           0.331               -1.09             -0.134                                 ok           False                  False
  SBUX           87.50                8            1.78              1.15         91.79                21.19         0.487 below_threshold              0.270              7.1                           0.203               -5.01             -0.458            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-10-13T11:10:06.032401-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:05:06.217854-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ISRG261120C00425000", "current_drop_pct": 0.98, "early_entry_score": 0.723, "early_reclaim_pct": 62.8, "entry_ask": 22.3, "entry_bid": 19.5, "entry_mode": "early", "entry_option_price": 20.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 34, "matched_signals": 30, "option_liquidity_status": "low_volume", "option_open_interest": 281.0, "option_spread_pct": 13.4, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.795, "shadow_only": true, "success_rate": 93.33, "ticker": "ISRG", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.723, "early_reclaim_pct": 62.8, "matched_signals": 30, "recovery_stability_score": 0.795, "success_rate": 93.33, "ticker": "ISRG", "timing_score": 0.454, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.71, "early_reclaim_pct": 63.9, "matched_signals": 42, "recovery_stability_score": 0.73, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:00:04.704921-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                             {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.59, "early_entry_score": 0.715, "early_reclaim_pct": 65.3, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.714, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.715, "early_reclaim_pct": 65.3, "matched_signals": 42, "recovery_stability_score": 0.714, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T10:55:05.723244-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:50:05.695677-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:45:04.655740-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:40:05.951817-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:35:04.412949-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "CEG261120C00290000", "fill_price": 21.65, "pnl": 9300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.09, "ticker": "CEG"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013111006)

</details>

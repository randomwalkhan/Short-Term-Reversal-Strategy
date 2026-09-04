# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 10:20:02 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$81,160.60`
- Equity: `$81,160.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-04)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261016C00110000     99          2026-09-03         2026-09-04        3.725         4.4 6682.5   18.120805 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               14            1.18              3.68        442.54                21.54         0.549          pass              0.609             42.4                           0.378               -0.10             -0.023                                 ok            True                  False
  PAYX          100.00               13            1.56              1.37        124.49                25.54         0.544          pass              0.604             43.1                           0.630               -1.08             -0.081                                 ok            True                  False
  NFLX           88.24               17            1.77              1.02         82.23                32.95         0.528          pass              0.338              6.4                           0.101                2.04              0.226                                 ok            True                  False
    ZS          100.00               18            2.94              3.66        176.23                62.66         0.523          pass              0.682             58.9                           0.518               -5.05             -0.042                                 ok            True                  False
 CMCSA           92.86               28            0.53              0.10         26.61                25.91         0.523          pass              0.588             24.3                           0.230               -1.27             -0.191                                 ok            True                  False
  WDAY           85.71               21            3.53              5.11        204.73                73.93         0.516          pass              0.378             33.5                           0.599               -0.19              0.309                                 ok            True                  False
  CHTR           90.70               43            0.61              0.65        151.10                61.35         0.509          pass              0.634             32.6                           0.186                0.19              0.033                                 ok            True                  False
  MSFT           88.24               17            1.57              5.61        507.72                22.07         0.501          pass              0.316              0.0                           0.169                3.90              0.390                                 ok            True                  False
  MNST           87.10               31            0.49              0.15         44.02               424.09         0.998          pass              0.579             50.0                           0.357               -8.21             -1.147 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00                5            3.08              1.23         56.29                56.63         0.604          pass              0.493             10.7                           0.239              -10.53             -1.600 downtrend_blocked_slope_and_streak           False                  False
  MSTR           76.19               21            4.03              4.08        143.07               101.55         0.556          pass              0.245             38.7                           0.377               16.55              1.216                                 ok           False                  False
  ABNB          100.00               14            1.88              2.44        184.21                64.22         0.541          pass              0.496              4.9                           0.191               -2.95             -0.398            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-04T10:20:02.325434-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.56, "early_entry_score": 0.68, "early_reclaim_pct": 62.8, "entry_ask": 16.5, "entry_bid": 14.4, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 40580.3, "hypothetical_contracts": 26, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 158.0, "option_spread_pct": 13.59, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.831, "shadow_only": true, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 1.56, "early_entry_score": 0.68, "early_reclaim_pct": 62.8, "matched_signals": 33, "recovery_stability_score": 0.831, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:15:04.189474-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:10:01.256246-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:10:01.256246-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "CSCO261016C00110000", "fill_price": 4.4, "pnl": 6682.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.12, "ticker": "CSCO"}
2026-09-04T10:05:05.442075-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:00:02.334638-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T00:00:05.130277-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
2026-09-03T15:10:05.000086-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T15:05:01.989817-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T14:55:01.997283-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904102002)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 10:40:01 EDT`
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

- Cash: `$47,718.10`
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.56              0.18         45.84               551.67         1.000          pass              0.576              0.0                           0.236                0.32             -0.112                      ok            True                  False
  TEAM           88.57               35            1.23              1.67        193.46               115.35         0.760          pass              0.664             64.3                           0.704               17.66              1.490                      ok            True                  False
  SHOP           92.00               25            2.10              2.17        146.44                69.51         0.595          pass              0.620             46.7                           0.805               -2.95              0.090                      ok            True                  False
  CSCO           81.48               27            1.21              0.93        110.09                40.87         0.552          pass              0.251             14.4                           0.263               -3.32             -0.105                      ok            True                  False
  DRAM           83.87               31            2.21              0.88         56.52                66.99         0.529          pass              0.369             24.4                           0.484                0.99              0.082                      ok            True                  False
  NVDA           86.21               29            1.22              1.88        219.69                45.52         0.523          pass              0.495             50.2                           0.617               -0.88              0.136                      ok            True                  False
   CSX           90.00               10            1.55              0.55         50.27                15.01         0.521          pass              0.344              8.5                           0.115               -1.69              0.014                      ok            True                  False
  CHTR           86.67               15            3.27              3.49        150.94                52.85         0.503          pass              0.326             21.4                           0.382                2.32              0.232                      ok            True                  False
  CPRT           86.49               37            0.67              0.15         32.92                40.13         0.501          pass              0.607             68.1                           0.760                3.38              0.126                      ok            True                  False
  IDXX           90.00               20            1.66              6.49        553.91                29.41         0.500          pass              0.464             27.0                           0.308                0.24             -0.037                      ok            True                  False
  INSM           87.18               39            0.62              0.53        121.59               109.80         0.786          pass              0.640             58.8                           0.531               -5.65             -0.682 downtrend_blocked_slope           False                  False
   WDC           77.78               36            0.28              0.88        450.17                84.65         0.671          pass              0.510             89.9                           0.793              -16.18             -1.171 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-01T10:40:01.982224-04:00 early_entry_1040 early_entry_shadow                                              {"contract_symbol": "INTU261016C00360000", "current_drop_pct": 0.77, "early_entry_score": 0.732, "early_reclaim_pct": 75.1, "entry_ask": 19.8, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 23859.05, "hypothetical_contracts": 12, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 493.0, "option_spread_pct": 11.76, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.884, "shadow_only": true, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.732, "early_reclaim_pct": 75.1, "matched_signals": 34, "recovery_stability_score": 0.884, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-01T10:35:04.145370-04:00 early_entry_1035 early_entry_shadow                                              {"contract_symbol": "INTU261016C00330000", "current_drop_pct": 0.83, "early_entry_score": 0.726, "early_reclaim_pct": 73.2, "entry_ask": 35.9, "entry_bid": 31.6, "entry_mode": "early", "entry_option_price": 33.75, "hypothetical_budget": 23859.05, "hypothetical_contracts": 7, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 179.0, "option_spread_pct": 12.74, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.853, "shadow_only": true, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.726, "early_reclaim_pct": 73.2, "matched_signals": 34, "recovery_stability_score": 0.853, "success_rate": 91.18, "ticker": "INTU", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-01T10:30:06.594545-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:25:01.815203-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:20:03.001967-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:15:02.023349-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:10:02.052599-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T10:05:04.005187-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ABNB261002C00182500", "current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 71.0, "entry_ask": 7.85, "entry_bid": 5.35, "entry_mode": "early", "entry_option_price": 6.6, "hypothetical_budget": 23859.05, "hypothetical_contracts": 36, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 37.88, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.606, "shadow_only": true, "success_rate": 93.75, "ticker": "ABNB", "timing_score": 0.658, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 71.0, "matched_signals": 32, "recovery_stability_score": 0.606, "success_rate": 93.75, "ticker": "ABNB", "timing_score": 0.658, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T10:00:06.717269-04:00 early_entry_1000 early_entry_shadow                  {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "entry_ask": 14.4, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 12.7, "hypothetical_budget": 23859.05, "hypothetical_contracts": 18, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 358.0, "option_spread_pct": 26.77, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.67, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "matched_signals": 36, "recovery_stability_score": 0.67, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T09:50:02.006317-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "SHOP261016C00150000", "fill_price": 7.38, "pnl": -2460.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901104001)

</details>

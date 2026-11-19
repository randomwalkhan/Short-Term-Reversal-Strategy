# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:50:02 EST`
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

- Cash: `$100,946.30`
- Equity: `$100,946.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00400000     15          2026-11-18         2026-11-19        33.15      29.835 -4972.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           91.43               35            1.37              3.76        389.30               121.61         0.760          pass              0.727             59.8                           0.555                8.27              0.382                                 ok            True                  False
  IDXX           96.43               28            1.21              5.91        695.94                78.12         0.712          pass              0.663             24.0                           0.383                2.88              0.196                                 ok            True                  False
  ABNB           82.61               23            1.54              1.94        179.38                55.20         0.574          pass              0.289             25.1                           0.321                4.30             -0.117                                 ok            True                  False
  COST           86.67               15            0.94              7.24       1093.52                23.52         0.563          pass              0.321             18.0                           0.225                1.94              0.438                                 ok            True                  False
  ODFL           84.21               19            1.63              2.00        174.25                43.99         0.558          pass              0.287             19.5                           0.184                1.00              0.366                                 ok            True                  False
  AAPL          100.00               19            1.05              2.60        351.34                27.20         0.553          pass              0.590             25.1                           0.282                1.40              0.209                                 ok            True                  False
   CEG           90.91               33            1.33              2.44        261.69                59.92         0.504          pass              0.619             41.5                           0.340                8.34              0.563                                 ok            True                  False
  ALNY           72.41               29            1.71              1.79        148.63               110.96         0.722          pass              0.233             11.4                           0.122               -6.27             -0.328 downtrend_blocked_slope_and_streak           False                  False
  AMAT           69.23               39            0.14              0.35        351.62                91.11         0.645          pass              0.514             85.3                           0.372               10.03              0.310                                 ok           False                  False
  REGN           87.50                8            2.47             16.37        938.52                54.27         0.627          pass              0.266              1.0                           0.215                2.13              0.435                                 ok           False                  False
   KDP           88.89                9            1.81              0.44         34.82                47.14         0.619          pass              0.393             31.4                           0.324               -6.82             -0.795            downtrend_blocked_slope           False                  False
  UPRO           84.62               26            1.12              0.98        124.98                70.38         0.605          pass              0.417             42.1                           0.237               -3.03             -0.574 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-19T10:50:02.655230-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:45:05.606696-05:00 early_entry_1045 early_entry_shadow {"contract_symbol": "TTWO270115C00220000", "current_drop_pct": 0.78, "early_entry_score": 0.677, "early_reclaim_pct": 83.7, "entry_ask": 14.3, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 13.4, "hypothetical_budget": 50473.15, "hypothetical_contracts": 37, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 4100.0, "option_spread_pct": 13.43, "option_volume": 120.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.711, "shadow_only": true, "success_rate": 88.24, "ticker": "TTWO", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.677, "early_reclaim_pct": 83.7, "matched_signals": 34, "recovery_stability_score": 0.711, "success_rate": 88.24, "ticker": "TTWO", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-19T10:40:04.606267-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:35:05.556374-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:30:04.546056-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:25:05.944079-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "APP270115C00400000", "fill_price": 29.835, "pnl": -4972.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-19T10:15:01.694448-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:10:05.743746-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119105002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119105002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119105002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119105002)

</details>

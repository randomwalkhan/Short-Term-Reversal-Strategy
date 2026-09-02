# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 11:20:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$23,958.10`
- Equity: `$48,078.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 24120.0         1.65           1.68       32.33         32.42          bid_ask_mid                       1.68                bid_ask_mid                    True           360.0                   1.52          87.5               16              1.99         38.72           39.45                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            2.08              1.82        124.10                86.77         0.579          pass              0.286             31.7                           0.224               17.30              1.546                                 ok            True                  False
  CSCO           88.89               36            0.72              0.55        109.50                36.37         0.511          pass              0.560             32.9                           0.242               -1.44             -0.071                                 ok            True                  False
  PAYX          100.00               16            1.32              1.16        125.14                25.34         0.509          pass              0.616             41.5                           0.316                1.21              0.222                                 ok            True                  False
    ZS          100.00               34            1.76              2.20        177.43                60.79         0.508          pass              0.734             40.9                           0.366               -5.08              0.110                                 ok            True                  False
  VRSK           85.71               14            2.38              3.24        192.96                34.83         0.503          pass              0.263             11.3                           0.186                1.75              0.329                                 ok            True                  False
  MNST           93.55               31            0.46              0.14         44.93               424.41         1.000          pass              0.821             73.4                           0.837               -5.58             -0.683            downtrend_blocked_slope           False                  False
  ABNB           93.10               29            0.80              1.02        182.11                64.48         0.666          pass              0.664             40.4                           0.341               -2.84             -0.277            downtrend_blocked_slope           False                  False
   APP           73.33               45            0.14              0.31        311.61                85.96         0.653          pass              0.544             92.8                           0.695                0.16              0.217                                 ok           False                  False
   WDC           78.57               28            1.98              6.26        447.76                82.26         0.598          pass              0.274             31.4                           0.416               -4.46             -0.287 downtrend_blocked_slope_and_streak           False                  False
  MRVL           78.12               32            2.40              3.54        208.87                79.24         0.538          pass              0.281             26.7                           0.281              -13.46             -1.707 downtrend_blocked_slope_and_streak           False                  False
  CRWD           80.00                5            4.63              6.97        212.08                87.98         0.535          pass              0.080              9.0                           0.198                1.73              1.462                                 ok           False                  False
   HON           80.00               25            0.76              1.12        209.50                29.51         0.521          pass              0.197             14.9                           0.184               -6.02             -0.412 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-02T11:20:05.322061-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:15:02.323157-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:10:02.511069-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:05:03.505803-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:59:24.886569-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:40:01.550864-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ZS261002C00177500", "current_drop_pct": 0.8, "early_entry_score": 0.872, "early_reclaim_pct": 73.3, "entry_ask": 14.9, "entry_bid": 12.75, "entry_mode": "early", "entry_option_price": 13.825, "hypothetical_budget": 11979.05, "hypothetical_contracts": 8, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 13.0, "option_spread_pct": 15.55, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.839, "shadow_only": true, "success_rate": 100.0, "ticker": "ZS", "timing_score": 0.525, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.872, "early_reclaim_pct": 73.3, "matched_signals": 41, "recovery_stability_score": 0.839, "success_rate": 100.0, "ticker": "ZS", "timing_score": 0.525, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-02T10:35:02.301132-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:30:05.379361-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:25:02.267090-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:20:01.429455-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902112005)

</details>

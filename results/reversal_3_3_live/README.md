# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 11:35:06 EDT`
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
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 24120.0         1.65           1.68       32.33         32.37          bid_ask_mid                       1.68                bid_ask_mid                    True           360.0                   1.52          87.5               16              1.99         38.72           39.89                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            2.19              1.91        124.06                86.77         0.573          pass              0.275             28.2                           0.286               17.17              1.541                                 ok            True                  False
    ZS          100.00               24            2.41              3.00        177.08                60.79         0.531          pass              0.605             19.4                           0.148               -5.70              0.081                                 ok            True                  False
  PAYX          100.00               15            1.45              1.27        125.09                25.34         0.508          pass              0.592             35.9                           0.263                1.08              0.216                                 ok            True                  False
  MNST           91.67               24            0.76              0.24         44.89               424.41         1.000          pass              0.672             55.8                           0.598               -5.86             -0.697            downtrend_blocked_slope           False                  False
  TEAM           92.86               42            0.14              0.19        186.95               117.24         0.775          pass              0.903             94.4                           0.431                7.19              1.184                                 ok           False                  False
  ABNB           94.29               35            0.35              0.44        182.36                64.48         0.659          pass              0.836             74.2                           0.664               -2.40             -0.256            downtrend_blocked_slope           False                  False
   WDC           81.82               33            1.10              3.48        448.95                82.26         0.625          pass              0.450             61.8                           0.806               -3.60             -0.247           downtrend_blocked_streak           False                  False
  MRVL           79.41               34            1.88              2.78        209.20                79.24         0.559          pass              0.343             42.5                           0.614              -13.00             -1.683 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               13            1.37              0.47         48.55                20.15         0.534          pass              0.542             23.0                           0.205               -6.53             -0.592 downtrend_blocked_slope_and_streak           False                  False
   HON           81.48               27            0.57              0.84        209.62                29.51         0.523          pass              0.314             36.4                           0.430               -5.84             -0.403 downtrend_blocked_slope_and_streak           False                  False
   STX           84.00               25            2.76             15.77        809.88                70.47         0.522          pass              0.341             27.3                           0.462               -4.62             -0.325 downtrend_blocked_slope_and_streak           False                  False
  INTU           89.29               28            1.34              3.23        343.54                46.23         0.515          pass              0.420              0.2                           0.051               -6.11             -0.603            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-02T11:35:06.484785-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:30:01.496570-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:25:02.340599-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:20:05.322061-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:15:02.323157-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:10:02.511069-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:05:03.505803-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:59:24.886569-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:40:01.550864-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ZS261002C00177500", "current_drop_pct": 0.8, "early_entry_score": 0.872, "early_reclaim_pct": 73.3, "entry_ask": 14.9, "entry_bid": 12.75, "entry_mode": "early", "entry_option_price": 13.825, "hypothetical_budget": 11979.05, "hypothetical_contracts": 8, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 13.0, "option_spread_pct": 15.55, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.839, "shadow_only": true, "success_rate": 100.0, "ticker": "ZS", "timing_score": 0.525, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.872, "early_reclaim_pct": 73.3, "matched_signals": 41, "recovery_stability_score": 0.839, "success_rate": 100.0, "ticker": "ZS", "timing_score": 0.525, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-02T10:35:02.301132-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902113506)

</details>

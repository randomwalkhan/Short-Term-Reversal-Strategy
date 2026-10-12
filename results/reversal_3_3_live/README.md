# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:50:05 EDT`
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

- Cash: `$58,874.30`
- Equity: `$120,474.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$3,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 61600.0         3.65           3.85       59.31         59.63          bid_ask_mid                       3.85                bid_ask_mid                    True          3200.0                   5.48          93.1               29              1.17         50.42            51.1                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           91.67               36            1.19              1.95        232.90                75.53         0.525            pass              0.688             50.4                           0.517               15.83              1.693                                 ok            True                  False
  ABNB           85.71               28            1.19              1.38        165.28                38.25         0.512            pass              0.417             31.2                           0.378                5.01              0.457                                 ok            True                  False
  MSTR           92.31               39            0.18              0.20        154.26                79.86         0.646            pass              0.838             84.1                           0.341               -1.96             -0.184                                 ok           False                  False
  SNPS           75.00               20            1.58              5.63        507.58                55.08         0.600            pass              0.135              2.8                           0.073               20.19              2.025                                 ok           False                  False
  QCOM           88.46               26            1.19              1.46        174.88                55.68         0.594            pass              0.505             37.7                           0.624               -7.50             -0.719 downtrend_blocked_slope_and_streak           False                  False
   STX           85.71               21            3.26             17.86        775.34                69.65         0.535            pass              0.292              4.2                           0.107              -17.80             -2.261            downtrend_blocked_slope           False                  False
 CMCSA           88.24               17            0.41              0.06         20.63                20.79         0.529            pass              0.460             46.9                           0.361               -4.11             -0.361            downtrend_blocked_slope           False                  False
   CEG           87.50               40            0.27              0.56        297.83                62.49         0.514            pass              0.683             77.2                           0.533               14.15              1.755                                 ok           False                  False
   WDC           73.08               26            2.60              7.23        394.18                64.73         0.508            pass              0.172              4.7                           0.081              -14.62             -1.843            downtrend_blocked_slope           False                  False
  DASH           76.92               13            2.66              3.66        194.93                43.05         0.508            pass              0.153             27.4                           0.464                7.22              0.723                                 ok           False                  False
  INTC           77.78               18            3.56              2.61        103.58                69.66         0.500 below_threshold              0.113              3.1                           0.195              -12.98             -1.479 downtrend_blocked_slope_and_streak           False                  False
  UPRO           86.49               37            0.21              0.22        155.62                29.53         0.493 below_threshold              0.528             41.8                           0.384                4.47              0.618                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-12T10:50:05.423702-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:45:04.583763-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:40:05.705407-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ADI261120C00420000", "current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "entry_ask": 14.3, "entry_bid": 12.9, "entry_mode": "early", "entry_option_price": 13.6, "hypothetical_budget": 29437.15, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 271.0, "option_spread_pct": 10.29, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.782, "shadow_only": true, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "matched_signals": 34, "recovery_stability_score": 0.782, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.677, "early_reclaim_pct": 67.4, "matched_signals": 37, "recovery_stability_score": 0.736, "success_rate": 89.19, "ticker": "ABNB", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T10:35:03.248275-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:30:04.278592-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:25:04.307064-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:20:06.400928-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:15:06.352070-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:10:05.611490-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:05:03.362660-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012105005)

</details>

# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:45:04 EDT`
Last processed slot: `early_entry_1045`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$18,164.25`
- Equity: `$33,124.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$860.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14960.0        35.25           37.4      477.34         475.5          bid_ask_mid                       37.4                bid_ask_mid                    True           860.0                    6.1         97.22               36              0.69         45.69           54.76                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.00               25            2.03              3.20        223.26               139.09         0.719            pass              0.543             17.2                           0.203               18.19              3.695                       ok            True                  False
  INTC           95.45               22            2.41              2.04        120.02                85.20         0.584            pass              0.559              6.7                           0.172                1.77              0.991                       ok            True                  False
  AMAT           89.66               29            0.86              2.70        448.52                50.48         0.553            pass              0.439              0.0                           0.150                1.32              0.612                       ok            True                  False
   TXN          100.00               14            1.82              4.02        314.23                35.59         0.533            pass              0.505              8.5                           0.230                0.66              0.478                       ok            True                  False
  NXPI           90.00               20            1.85              4.27        328.45                46.79         0.506            pass              0.385              0.3                           0.104               10.20              1.467                       ok            True                  False
  INSM           77.78               45            0.12              0.09        108.33               111.11         0.778            pass              0.549             90.5                           0.799               -6.38             -0.334                       ok           False                  False
  MSTR           85.71               42            0.01              0.01        151.63                63.23         0.548            pass              0.705             99.4                           0.780              -18.91             -1.821  downtrend_blocked_slope           False                  False
   AEP           87.50               32            0.04              0.04        127.74                25.60         0.528            pass              0.684             94.8                           0.845               -0.70              0.130                       ok           False                  False
  GOOG           87.50                8            2.28              6.15        383.48                41.01         0.522            pass              0.275              7.8                           0.116               -5.00             -0.372  downtrend_blocked_slope           False                  False
 GOOGL           87.50                8            2.41              6.57        387.31                41.30         0.520            pass              0.263              3.7                           0.093               -5.07             -0.362  downtrend_blocked_slope           False                  False
  AMGN           91.43               35            0.15              0.35        336.33                27.03         0.500            pass              0.778             85.4                           0.741                0.68              0.288                       ok           False                  False
   CSX           63.64               11            1.58              0.51         45.59                23.65         0.490 below_threshold              0.115             19.9                           0.264               -1.82             -0.004 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-29T10:45:04.066585-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:40:02.188936-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:35:01.212926-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:30:02.245861-04:00 early_entry_1030                   entry {"allocated_cash": 14100.0, "asset_type": "option", "contract_symbol": "SNPS260717C00470000", "contracts": 4, "early_entry_score": 0.826, "entry_mode": "early", "entry_option_price": 35.25, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 115.0, "option_spread_pct": 11.06, "option_volume": 67.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.401}
2026-05-29T10:25:01.208564-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:25:01.208564-04:00 early_entry_1025 entry_candidate_skipped                                                                                                                                                                       {"early_entry_score": 0.814, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 18.61, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.395}
2026-05-29T10:20:01.218195-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:20:01.218195-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                                       {"early_entry_score": 0.816, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 19.35, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.396}
2026-05-29T10:15:06.109113-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:15:06.109113-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                             {"early_entry_score": 0.716, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 15.24, "option_volume": 10.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.402}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529104504)

</details>

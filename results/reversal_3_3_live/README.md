# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 10:00:03 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$19,710.25`
- Equity: `$28,910.25`
- Realized PnL: `$19,085.25`
- Unrealized PnL: `$-175.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                  9200.0        46.88           46.0      660.72        662.37     last_price_stale                        NaN                unavailable                   False          -175.0                  -1.87         81.82               22              1.27         53.38             0.0                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15        11.55       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           86.67               15            0.96              0.34         49.78                19.08         0.566          pass              0.285              5.9                           0.118                4.02              0.351                                 ok            True                  False
  SOXL           87.10               31            0.81              1.00        176.23               219.49         0.927          pass              0.637             71.8                           0.374              -34.30             -2.790            downtrend_blocked_slope           False                  False
  KLAC           84.00               25            1.70              2.74        229.20               109.33         0.709          pass              0.380             34.1                           0.251              -24.94             -1.987 downtrend_blocked_slope_and_streak           False                  False
  DRAM           85.00               20            3.28              1.41         60.63               112.33         0.701          pass              0.330             19.9                           0.240              -10.08             -0.764            downtrend_blocked_slope           False                  False
    MU           82.61               23            2.94             20.23        974.45               112.73         0.697          pass              0.278             17.3                           0.182              -17.32             -1.184            downtrend_blocked_slope           False                  False
  AMAT           88.89               27            1.00              4.16        593.92                98.89         0.693          pass              0.588             56.2                           0.360              -18.43             -1.297 downtrend_blocked_slope_and_streak           False                  False
  LRCX           88.89               27            1.32              3.21        344.73                98.70         0.681          pass              0.565             48.9                           0.323              -21.19             -1.664 downtrend_blocked_slope_and_streak           False                  False
   WDC           88.24               17            4.15             16.36        556.31               117.61         0.654          pass              0.361              9.8                           0.171              -15.46             -0.877            downtrend_blocked_slope           False                  False
  MDLZ           93.75               16            0.36              0.15         58.74                30.54         0.627          pass              0.701             77.2                           0.666                1.30             -0.076                                 ok           False                  False
  MRVL           89.29               28            2.51              3.91        220.76               101.70         0.615          pass              0.550             40.1                           0.395              -27.19             -2.668            downtrend_blocked_slope           False                  False
  INTC           88.24               34            1.40              1.06        107.31                89.50         0.579          pass              0.529             30.6                           0.238              -23.91             -2.430            downtrend_blocked_slope           False                  False
   PEP           93.10               29            0.09              0.08        135.41                30.60         0.574          pass              0.786             84.0                           0.617               -0.05             -0.390                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-07-15T10:00:03.493578-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "AAPL260821C00315000", "fill_price": 13.45, "pnl": 2090.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.45, "ticker": "AAPL"}
2026-07-15T09:35:02.740173-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:30:04.740888-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:25:03.806265-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:20:04.874058-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:15:04.885771-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:10:05.907681-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:05:04.903172-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:00:02.786687-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715100003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715100003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715100003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715100003)

</details>

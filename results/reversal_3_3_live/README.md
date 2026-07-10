# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 09:36:17 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$14,359.25`
- Equity: `$29,431.25`
- Realized PnL: `$18,399.25`
- Unrealized PnL: `$1,032.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00135000       2026-07-09                   1     24     14040.0                 15072.0         5.85           6.28      133.88        133.15     last_price_stale                        NaN                unavailable                   False          1032.0                   7.35         93.33               15              1.42          35.3            1.56                  35.14                8090.0           34.0               0.07                      ok
```

## Today's Closed Trades (2026-07-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.00               30            0.95              2.06        307.65                66.26         0.613          pass              0.650             62.9                           0.506               -1.99              0.325                                 ok            True                  False
  NXPI           86.67               30            1.01              2.05        289.66                60.34         0.588          pass              0.511             47.1                           0.550               -3.69              0.008                                 ok            True                  False
   ADI           87.88               33            0.78              2.15        392.72                58.62         0.574          pass              0.652             76.9                           0.707               -6.55             -0.375                                 ok            True                  False
  GILD           87.50               16            1.26              1.19        134.33                34.25         0.547          pass              0.340             15.2                           0.257                7.51              0.884                                 ok            True                  False
  AVGO           86.84               38            0.50              1.41        400.51                53.79         0.537          pass              0.604             60.3                           0.686                5.33              0.673                                 ok            True                  False
  VRTX           94.74               19            1.23              4.26        494.67                34.73         0.511          pass              0.542             12.6                           0.301                2.13              0.274                                 ok            True                  False
  SOXL           86.36               22            4.24              5.71        190.00               230.34         0.885          pass              0.442             34.5                           0.525              -27.04             -3.642            downtrend_blocked_slope           False                  False
  KLAC           88.00               25            1.46              2.35        228.49               118.44         0.767          pass              0.390              0.0                             NaN              -12.62             -2.255 downtrend_blocked_slope_and_streak           False                  False
   WDC           81.48               27            1.30              5.25        575.80               123.00         0.766          pass              0.411             60.4                           0.727              -15.52             -1.646            downtrend_blocked_slope           False                  False
    MU           80.00               25            2.03             14.10        985.60               119.39         0.751          pass              0.295             40.1                           0.480              -19.93             -2.424            downtrend_blocked_slope           False                  False
  DRAM           82.35               17            3.76              1.69         63.61               119.54         0.719          pass              0.223             13.9                           0.349              -19.47             -2.165            downtrend_blocked_slope           False                  False
   STX           91.67               36            0.46              2.87        888.86                96.96         0.677          pass              0.814             87.2                           0.757              -13.59             -1.355            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-10T00:00:05.149826-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-07-09T15:10:06.797522-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:05:11.506156-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:00:11.129710-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:55:10.687527-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:50:10.393351-04:00       entry_1500              entry {"allocated_cash": 14040.0, "asset_type": "option", "contract_symbol": "GILD260821C00135000", "contracts": 24, "early_entry_score": 0.621, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 8090.0, "option_spread_pct": 6.84, "option_volume": 34.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.541}
2026-07-09T14:50:10.393351-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-09", "training_samples": 5465, "window": 5}
2026-07-09T12:00:04.046756-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:55:06.157143-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:50:05.085430-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710093617)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710093617)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710093617)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710093617)

</details>

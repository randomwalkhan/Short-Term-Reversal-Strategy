# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 09:40:05 EDT`
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

- Cash: `$23,958.10`
- Equity: `$56,358.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$8,640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 32400.0         1.65           2.25       32.33         31.99     last_price_stale                        NaN                unavailable                   False          8640.0                  36.36          87.5               16              1.99         38.72            1.56                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           81.25               32            1.57              1.38        124.29                86.77         0.599          pass              0.385             48.3                           0.428               17.90              1.569                                 ok            True                  False
    ZS          100.00               27            2.21              2.76        177.19                60.79         0.524          pass              0.643             25.8                           0.316               -5.51              0.090                                 ok            True                  False
  PAYX          100.00               11            1.81              1.59        124.96                25.34         0.511          pass              0.517             19.9                           0.315                0.71              0.199                                 ok            True                  False
  VRSK           86.67               15            2.32              3.16        193.00                34.83         0.502          pass              0.302             13.6                           0.246                1.82              0.332                                 ok            True                  False
  MNST           88.24               17            1.14              0.36         44.84               424.41         1.000          pass              0.429             20.8                           0.259               -6.23             -0.715            downtrend_blocked_slope           False                  False
  SOXL           83.33               36            0.30              0.22        105.65                97.59         0.688          pass              0.612             93.5                           0.949              -12.68             -1.260            downtrend_blocked_slope           False                  False
  ABNB           96.00               25            1.14              1.46        181.92                64.48         0.673          pass              0.612             14.8                           0.245               -3.18             -0.293            downtrend_blocked_slope           False                  False
   APP           71.05               38            1.20              2.61        310.62                85.96         0.631          pass              0.365             38.6                           0.323               -0.89              0.169                                 ok           False                  False
  MRVL           79.41               34            1.30              1.92        209.57                79.24         0.595          pass              0.396             59.0                           0.682              -12.49             -1.656 downtrend_blocked_slope_and_streak           False                  False
  MELI          100.00               36            0.46              6.37       1960.76                49.25         0.580          pass              0.784             50.8                           0.376                2.40              0.191                                 ok           False                  False
  CRWD           75.00               12            3.36              5.06        212.90                87.98         0.573          pass              0.122             17.2                           0.247                3.08              1.522                                 ok           False                  False
   AEP           77.78                9            0.98              0.85        122.60                17.91         0.560          pass              0.093             12.5                           0.184               -3.58             -0.208                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                                                              detail
2026-09-02T09:40:05.355091-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:35:05.293548-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:30:01.390795-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00  manage_0930 exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T00:00:06.180126-04:00 data_refresh data_refresh                                                                                                                                                                                                       {'saved': 93}
2026-09-01T15:10:01.952718-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-01T15:05:02.102329-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-01T15:00:06.883715-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-01T14:55:03.896264-04:00   entry_1500 slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902094005)

</details>

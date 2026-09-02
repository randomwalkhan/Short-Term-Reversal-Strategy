# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 09:45:03 EDT`
Last processed slot: `manual`

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
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23760.0         1.65           1.65       32.33         32.05          bid_ask_mid                       1.65                bid_ask_mid                    True             0.0                    0.0          87.5               16              1.99         38.72           59.38                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   AEP           86.67               15            0.81              0.70        122.66                17.91         0.545          pass              0.349             27.6                           0.288               -3.41             -0.200                                 ok            True                  False
    ZS          100.00               24            2.41              3.01        177.08                60.79         0.530          pass              0.604             19.1                           0.243               -5.71              0.080                                 ok            True                  False
  SNPS           89.19               37            0.84              2.45        413.77                58.04         0.526          pass              0.655             59.1                           0.437                2.51              0.862                                 ok            True                  False
  PAYX          100.00               13            1.48              1.31        125.08                25.34         0.518          pass              0.575             34.3                           0.440                1.04              0.214                                 ok            True                  False
  ADBE           82.35               34            0.85              1.70        285.35                41.02         0.501          pass              0.417             48.0                           0.376                4.10              0.678                                 ok            True                  False
  MNST           86.67               15            1.27              0.40         44.82               424.41         1.000          pass              0.358             15.6                           0.265               -6.35             -0.720            downtrend_blocked_slope           False                  False
  ABNB           96.43               28            0.91              1.16        182.05                64.48         0.669          pass              0.684             32.2                           0.278               -2.95             -0.282            downtrend_blocked_slope           False                  False
  SOXL           82.86               35            1.01              0.75        105.43                97.59         0.651          pass              0.542             78.1                           0.867              -13.30             -1.293            downtrend_blocked_slope           False                  False
   APP           72.09               43            0.58              1.27        311.20                85.96         0.640          pass              0.474             70.1                           0.566               -0.28              0.197                                 ok           False                  False
  MSTR           85.00               40            0.19              0.17        124.81                86.77         0.638          pass              0.678             93.7                           0.655               19.56              1.632                                 ok           False                  False
  MELI          100.00               38            0.38              5.28       1961.23                49.25         0.573          pass              0.822             59.2                           0.371                2.48              0.194                                 ok           False                  False
  MRVL           79.41               34            1.67              2.46        209.34                79.24         0.573          pass              0.360             47.5                           0.620              -12.81             -1.673 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902094503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902094503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902094503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902094503)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 09:30:01 EDT`
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
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 32400.0         1.65           2.25       32.33         32.24     last_price_stale                        NaN                unavailable                   False          8640.0                  36.36          87.5               16              1.99         38.72            0.78                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.33               36            1.25              1.09        124.41                86.77         0.597          pass              0.499             59.1                           0.442               18.30              1.584                                 ok            True                  False
  MELI          100.00               33            0.70              9.63       1959.36                49.25         0.585          pass              0.689             25.6                           0.307                2.15              0.180                                 ok            True                  False
    ZS          100.00               38            1.20              1.50        177.73                60.79         0.529          pass              0.749             36.5                           0.450               -4.53              0.136                                 ok            True                  False
  PAYX          100.00               12            1.59              1.40        125.04                25.34         0.524          pass              0.466              0.0                           0.371                0.93              0.209                                 ok            True                  False
   TRI           94.29               35            0.65              0.48        106.14                53.71         0.502          pass              0.598              0.0                           0.250                0.68              0.056                                 ok            True                  False
  INSM           88.89               36            0.92              0.78        121.17               110.63         0.794          pass              0.529             13.2                           0.211               -7.86             -0.665            downtrend_blocked_slope           False                  False
  ABNB           93.94               33            0.39              0.50        183.00                64.48         0.661          pass              0.824             77.6                           0.529               -2.09             -0.242                                 ok           False                  False
   APP           72.09               43            0.63              1.36        311.16                85.96         0.641          pass              0.441             58.9                           0.412               -0.32              0.195                                 ok           False                  False
   STX           87.10               31            1.06              6.07        814.04                70.47         0.626          pass              0.572             60.0                           0.537               -2.95             -0.247           downtrend_blocked_streak           False                  False
  SOXL           82.86               35            1.55              1.14        105.25                97.59         0.621          pass              0.504             66.4                           0.688              -13.77             -1.318            downtrend_blocked_slope           False                  False
   WDC           78.57               28            2.03              6.41        447.69                82.26         0.613          pass              0.235             17.8                           0.353               -4.50             -0.290 downtrend_blocked_slope_and_streak           False                  False
  MCHP           90.00               40            0.13              0.06         71.38                59.53         0.604          pass              0.806             93.1                           0.674               -6.92             -0.608            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                detail
2026-09-02T09:30:01.390795-04:00  manage_0930            exit_skipped                                                   {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00  manage_0930            exit_skipped                                                   {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00  manage_0930            exit_skipped                                                   {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T00:00:06.180126-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                         {'saved': 93}
2026-09-01T15:10:01.952718-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T15:05:02.102329-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T15:00:06.883715-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:55:03.896264-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:50:05.175915-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.709, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 25.0, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.593}
2026-09-01T14:50:05.175915-04:00   entry_1500          timing_overlay                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-01", "training_samples": 5739, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902093001)

</details>

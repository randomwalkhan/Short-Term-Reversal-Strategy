# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 09:35:05 EDT`
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
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 32400.0         1.65           2.25       32.33         32.16     last_price_stale                        NaN                unavailable                   False          8640.0                  36.36          87.5               16              1.99         38.72            0.78                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS          100.00               35            1.54              1.93        177.54                60.79         0.523          pass              0.712             31.0                           0.397               -4.87              0.121                                 ok            True                  False
  COST           89.47               19            0.99              6.51        937.17                19.36         0.523          pass              0.426             20.5                           0.268               -2.75             -0.186                                 ok            True                  False
  PAYX          100.00               13            1.49              1.31        125.08                25.34         0.520          pass              0.553             27.0                           0.313                1.04              0.214                                 ok            True                  False
  MNST           86.67               15            1.29              0.41         44.82               424.41         1.000          pass              0.330              6.5                           0.213               -6.37             -0.721            downtrend_blocked_slope           False                  False
  ABNB           93.55               31            0.56              0.71        182.24                64.48         0.669          pass              0.743             58.4                           0.511               -2.61             -0.266            downtrend_blocked_slope           False                  False
   WDC           81.82               33            1.04              3.28        449.03                82.26         0.646          pass              0.440             57.9                           0.585               -3.54             -0.244           downtrend_blocked_streak           False                  False
   STX           88.57               35            0.37              2.10        815.74                70.47         0.640          pass              0.718             86.1                           0.803               -2.27             -0.215           downtrend_blocked_streak           False                  False
   APP           69.44               36            1.52              3.32        310.32                85.96         0.623          pass              0.279             14.6                           0.168               -1.22              0.154                                 ok           False                  False
  SOXL           82.35               34            1.69              1.25        105.21                97.59         0.618          pass              0.474             63.3                           0.689              -13.90             -1.324            downtrend_blocked_slope           False                  False
  CRWD           75.00               12            3.40              5.12        212.88                87.98         0.571          pass              0.120             16.4                           0.314                3.04              1.520                                 ok           False                  False
  MSTR           77.78               27            2.54              2.22        123.93                86.77         0.567          pass              0.220             16.6                           0.196               16.75              1.524                                 ok           False                  False
  MRVL           79.41               34            1.80              2.65        209.26                79.24         0.565          pass              0.347             43.5                           0.562              -12.92             -1.679 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-02T09:35:05.293548-04:00  manage_0930 exit_skipped                                                                                                                                                                                                                   {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:30:01.390795-04:00  manage_0930 exit_skipped                                                                                                                                                                                                                   {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00  manage_0930 exit_skipped                                                                                                                                                                                                                   {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00  manage_0930 exit_skipped                                                                                                                                                                                                                   {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T00:00:06.180126-04:00 data_refresh data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-09-01T15:10:01.952718-04:00   entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T15:05:02.102329-04:00   entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T15:00:06.883715-04:00   entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:55:03.896264-04:00   entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-01T14:50:05.175915-04:00   entry_1500        entry {"allocated_cash": 23760.0, "asset_type": "option", "contract_symbol": "CPRT261016C00032500", "contracts": 144, "early_entry_score": 0.311, "entry_mode": "regular", "entry_option_price": 1.65, "execution_mode": "option", "matched_signals": 16, "option_liquidity_status": "ok", "option_open_interest": 398.0, "option_spread_pct": 6.06, "option_volume": 105.0, "success_rate": 87.5, "ticker": "CPRT", "timing_score": 0.554}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902093505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902093505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902093505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902093505)

</details>

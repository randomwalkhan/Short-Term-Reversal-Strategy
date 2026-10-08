# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 09:50:06 EDT`
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

- Cash: `$47,804.30`
- Equity: `$106,241.80`
- Realized PnL: `$89,916.80`
- Unrealized PnL: `$6,325.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   2     55     52112.5                 58437.5         9.48          10.62      160.14        162.49          bid_ask_mid                      10.62                bid_ask_mid                    True          6325.0                  12.14         83.33               12               2.4         42.26           47.33                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           86.96               23            2.16             21.58       1416.73                55.22         0.556            pass              0.345              5.8                           0.224                4.62              0.826                                 ok            True                  False
  AMGN           81.25               16            1.10              3.17        411.72                28.61         0.542            pass              0.216             29.7                           0.266                0.62             -0.220                                 ok            True                  False
   ADI           83.33               18            1.54              4.42        408.18                34.70         0.535            pass              0.270             24.7                           0.336                5.53              0.700                                 ok            True                  False
  AVGO           80.00               15            2.34              6.17        373.87                34.55         0.502            pass              0.102              6.1                           0.187                4.95              0.701                                 ok            True                  False
  UPRO           82.76               29            0.79              0.86        154.79                30.53         0.500 below_threshold              0.419             56.2                           0.693                2.63              0.420                                 ok            True                  False
  MSTR           88.46               26            2.78              2.98        152.09                80.80         0.577            pass              0.461             23.8                           0.258               -7.73             -0.211           downtrend_blocked_streak           False                  False
  CSCO           89.29               28            0.35              0.29        117.27                34.80         0.567            pass              0.635             70.3                           0.739                9.78              1.214                                 ok           False                  False
  QCOM           87.50               24            2.04              2.53        176.04                56.66         0.567            pass              0.379              9.5                           0.176              -10.68             -1.115 downtrend_blocked_slope_and_streak           False                  False
  META           85.71               42            0.03              0.18        721.23                52.76         0.550            pass              0.701             97.8                           0.567               -7.27             -0.394            downtrend_blocked_slope           False                  False
   WDC           80.00               30            1.66              4.71        403.40                65.89         0.543            pass              0.254             22.0                           0.222              -11.46             -1.384            downtrend_blocked_slope           False                  False
   STX           88.89               27            2.42             13.69        801.70                69.74         0.540            pass              0.431              8.8                           0.134              -13.02             -1.590            downtrend_blocked_slope           False                  False
 CMCSA           90.91               22            0.12              0.02         20.93                21.76         0.522            pass              0.685             87.2                           0.609               -4.02             -0.335            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-08T09:50:06.393850-04:00  manage_1000                    exit                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "NVDA261120C00235000", "fill_price": 11.7675, "pnl": -5230.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "NVDA"}
2026-10-08T00:00:04.872922-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 91, 'empty': 2}
2026-10-07T15:10:05.672351-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:05:05.765684-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:00:04.880221-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:55:05.726912-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:50:06.730595-04:00   entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-07", "training_samples": 5970, "window": 5}
2026-10-07T14:50:06.730595-04:00   entry_1500                   entry {"allocated_cash": 52300.0, "asset_type": "option", "contract_symbol": "NVDA261120C00235000", "contracts": 40, "early_entry_score": 0.461, "entry_mode": "regular", "entry_option_price": 13.075, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 17037.0, "option_spread_pct": 1.15, "option_volume": 1205.0, "success_rate": 90.91, "ticker": "NVDA", "timing_score": 0.512}
2026-10-07T14:50:06.730595-04:00   entry_1500 entry_candidate_skipped                                                                                                                                                                                 {"early_entry_score": 0.14, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.522}
2026-10-07T14:50:06.730595-04:00   entry_1500 entry_candidate_skipped                                                                                                                                                                                                   {"early_entry_score": 0.49, "option_liquidity_status": "low_volume", "option_open_interest": 993.0, "option_spread_pct": 12.24, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.545}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008095006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008095006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008095006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008095006)

</details>

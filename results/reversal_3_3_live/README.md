# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 11:10:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$4,051.00`
- Equity: `$32,006.00`
- Realized PnL: `$21,986.00`
- Unrealized PnL: `$20.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15475.0        29.05          30.95      350.60        349.97          bid_ask_mid                      30.95                bid_ask_mid                    True           950.0                   6.54         97.30               37              0.63         45.67           50.89                  37.94                2023.0           40.0               0.13                      ok
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 12480.0        44.70          41.60      510.62        493.64          bid_ask_mid                      41.60                bid_ask_mid                    True          -930.0                  -6.94         97.14               35              0.50         52.16           64.88                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.00               30            1.06              2.19        293.23                90.16         0.724          pass              0.406             66.7                           0.619               -1.42              0.025                                 ok            True                  False
   TXN           92.00               25            1.00              2.15        307.25                67.99         0.689          pass              0.706             72.5                           0.587                9.12              1.062                                 ok            True                  False
  SNPS          100.00               11            3.21             11.44        505.12                41.57         0.544          pass              0.468              2.4                           0.065                0.95              0.221                                 ok            True                  False
 GOOGL           88.57               35            0.56              1.57        400.40                40.65         0.534          pass              0.670             73.9                           0.648                3.41              0.344                                 ok            True                   True
  GOOG           89.19               37            0.54              1.49        396.53                40.76         0.526          pass              0.698             73.4                           0.623                3.08              0.332                                 ok            True                   True
  CDNS           97.30               37            0.81              2.01        351.98                37.94         0.510          pass              0.811             59.9                           0.408                2.65              0.195                                 ok            True                  False
  CHTR           66.67               12            3.25              3.37        146.56               114.29         0.707          pass              0.177             30.9                           0.252              -16.62             -1.680            downtrend_blocked_slope           False                  False
 CMCSA           90.62               32            0.28              0.05         25.15                60.26         0.668          pass              0.563             22.2                           0.160               -7.69             -0.942 downtrend_blocked_slope_and_streak           False                  False
  GEHC           55.00               20            1.78              0.78         62.34                57.53         0.592          pass              0.216             29.9                           0.235                0.86              0.196                                 ok           False                  False
  INTC          100.00                2            6.18              5.01        113.78               111.79         0.590          pass              0.542             27.7                           0.378                9.18              1.653                                 ok           False                  False
  MELI           81.82               11            2.62             29.50       1594.73                58.02         0.586          pass              0.114              0.0                           0.218              -15.40             -2.057            downtrend_blocked_slope           False                  False
   XEL           91.67               12            1.55              0.87         79.66                24.20         0.565          pass              0.417             12.1                           0.313               -4.59             -0.330            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-15T11:10:04.211296-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T11:05:04.217696-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T11:00:05.390084-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:55:04.100799-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:50:04.174954-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:45:04.262629-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:40:01.261107-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:35:04.245705-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:30:01.313959-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:25:04.076553-04:00 early_entry_1025 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515111004)

</details>

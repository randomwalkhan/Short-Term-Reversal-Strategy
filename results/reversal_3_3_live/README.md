# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 10:20:01 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$30,526.00`
- Realized PnL: `$21,986.00`
- Unrealized PnL: `$-1,460.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 14175.0        29.05          28.35      350.60        351.04          bid_ask_mid                      28.35                bid_ask_mid                    True          -350.0                  -2.41         97.30               37              0.63         45.67           40.00                  37.94                2023.0           40.0               0.13                      ok
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 12300.0        44.70          41.00      510.62        506.80          bid_ask_mid                      41.00                bid_ask_mid                    True         -1110.0                  -8.28         97.14               35              0.50         52.16           51.58                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.65               31            1.02              2.11        293.27                90.16         0.721          pass              0.433             67.9                           0.805               -1.38              0.026                                 ok            True                  False
   TXN           93.10               29            0.69              1.50        307.53                67.99         0.684          pass              0.787             80.8                           0.838                9.45              1.076                                 ok            True                  False
  SNPS           97.14               35            0.63              2.26        509.05                41.57         0.552          pass              0.825             67.8                           0.738                3.63              0.340                                 ok            True                   True
 GOOGL           88.89               36            0.55              1.55        400.41                40.65         0.529          pass              0.686             74.2                           0.778                3.41              0.345                                 ok            True                   True
  CDNS           97.30               37            0.51              1.26        352.30                37.94         0.528          pass              0.857             74.9                           0.822                2.96              0.209                                 ok            True                   True
  GOOG           89.19               37            0.52              1.44        396.55                40.76         0.528          pass              0.701             74.4                           0.746                3.11              0.333                                 ok            True                   True
  CHTR           71.43               14            3.04              3.15        146.65               114.29         0.712          pass              0.204             35.3                           0.477              -16.44             -1.671            downtrend_blocked_slope           False                  False
  INSM           50.00               16            2.92              2.37        114.61               110.45         0.651          pass              0.179             24.7                           0.407              -15.77             -2.245 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           92.50               40            0.04              0.01         25.17                60.26         0.637          pass              0.864             88.9                           0.376               -7.47             -0.931 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00                8            5.29              4.29        114.09               111.79         0.604          pass              0.575             38.1                           0.653               10.22              1.696                                 ok           False                  False
  GEHC           61.54               26            1.40              0.62         62.41                57.53         0.585          pass              0.299             44.7                           0.395                1.25              0.214                                 ok           False                  False
   XEL           92.31               13            1.26              0.70         79.73                24.20         0.580          pass              0.442             11.8                           0.220               -4.30             -0.316            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-15T10:20:01.244544-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:15:04.078787-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:10:04.236759-04:00 early_entry_1010         entry {"allocated_cash": 14525.0, "asset_type": "option", "contract_symbol": "CDNS260618C00330000", "contracts": 5, "early_entry_score": 0.838, "entry_mode": "early", "entry_option_price": 29.05, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2023.0, "option_spread_pct": 13.43, "option_volume": 40.0, "success_rate": 97.3, "ticker": "CDNS", "timing_score": 0.521}
2026-05-15T10:10:04.236759-04:00      manage_1000          exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 29.115, "pnl": -1617.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-15T10:05:04.229030-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "max_open_positions"}
2026-05-15T10:00:02.295451-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "max_open_positions"}
2026-05-15T00:00:05.036344-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 92}
2026-05-14T15:10:04.841035-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-14T15:05:08.308131-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-14T15:00:08.187447-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515102001)

</details>

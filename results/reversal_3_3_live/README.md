# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 09:30:03 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,922.50`
- Equity: `$14,832.50`
- Realized PnL: `$4,997.50`
- Unrealized PnL: `$-165.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260529C00084000       2026-04-28                   1     10      7075.0                  6910.0         7.08           6.91       84.22          86.6          -165.0                  -2.33         100.0               38              0.91         70.58             0.0                  91.28                 369.0           78.0               0.05                      ok
```

## Today's Closed Trades (2026-04-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  AXON           81.82               44            0.57              1.62        405.62                69.13            True
    ZS           82.76               29            1.55              1.48        135.44                65.17            True
  NFLX           86.21               29            0.98              0.63         92.02                46.23            True
  TEAM           85.42               48            0.56              0.27         69.59                78.64            True
  SNPS           94.44               36            0.91              3.09        482.56                50.93            True
  ISRG           91.67               24            1.20              3.91        464.97                36.73            True
  FAST           91.18               34            0.68              0.21         44.58                39.66            True
  CDNS           94.59               37            0.90              2.05        324.45                53.80            True
  PLTR           82.61               23            2.37              2.34        140.18                59.63            True
  WDAY           81.08               37            1.53              1.30        120.62                63.12            True
  DDOG           90.00               30            1.61              1.48        130.91                52.25            True
  MSTR           85.00               40            1.17              1.36        165.13                66.76            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-29T09:30:03.967315-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T09:25:06.961152-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T00:01:06.010136-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-28T16:10:03.932296-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-28T16:05:04.331443-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-28T16:00:09.270928-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-28T15:55:07.558006-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-28T15:40:04.250884-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-28T15:35:04.434156-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-28T15:30:04.969222-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429093003)

</details>

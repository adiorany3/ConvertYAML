# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 12
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 18

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=203ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=201ms, nekobox=253ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-97MS`
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-86MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-391MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-407MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-404MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-407MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-413MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-383MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-347MS` (url=734ms, status=HTTP 204)
12. `AKUN-025-UNKNOWN-VLESS-WS-656MS` (url=1171ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

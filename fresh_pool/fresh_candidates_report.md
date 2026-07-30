# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=251ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=268ms, nekobox=265ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=223ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=275ms, nekobox=272ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=252ms, nekobox=276ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=248ms, nekobox=170ms, status=no)
7. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-85MS`
9. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-73MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-69MS` (url=257ms, nekobox=177ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-110MS`
13. `AKUN-015-CLOUDFLARE-VLESS-WS-171MS` (url=347ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-156MS` (url=350ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-132MS` (url=250ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-271MS` (url=648ms, status=HTTP 204)
17. `AKUN-020-TW-CLOUD-VLESS-WS-279MS` (url=4782ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-345MS` (url=762ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-461MS` (url=721ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-65MS` (url=698ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-583MS` (url=1334ms, status=HTTP 204)
22. `AKUN-032-NET-141-11-202-0-23-VLESS-WS-258MS` (url=547ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

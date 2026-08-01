# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=341ms, nekobox=408ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=316ms, nekobox=360ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=328ms, nekobox=348ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS` (url=340ms, nekobox=408ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=355ms, nekobox=198ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=276ms, nekobox=7178ms, status=no)
7. `AKUN-005-UNKNOWN-VLESS-WS-95MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS` (url=385ms, nekobox=252ms, status=no)
9. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS`
10. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS`
13. `AKUN-010-090227-VLESS-WS-149MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=338ms, status=HTTP 204)
15. `AKUN-016-LEVIKOGJGFDD-VLESS-WS-111MS` (url=358ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-141MS` (url=422ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-160MS` (url=316ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-137MS` (url=526ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-207MS` (url=435ms, status=HTTP 204)
20. `AKUN-021-DE-CLOUDKLEYER-20190515-VLESS-WS-183MS` (url=449ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-295MS` (url=623ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-411MS` (url=810ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-522MS` (url=792ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-530MS` (url=939ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-617MS` (url=4666ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-110MS`
2. `AKUN-002-UNKNOWN-VLESS-WS-91MS`
3. `AKUN-003-UNKNOWN-VLESS-WS-119MS`
4. `AKUN-006-CLOUDFLARE-VLESS-WS-114MS` (url=304ms, nekobox=220ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-119MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-130MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-133MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS`
9. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=322ms, nekobox=216ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-133MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-139MS`
12. `AKUN-010-ZENFO-1-VLESS-WS-147MS`
13. `AKUN-016-CLOUDFLARE-VLESS-WS-179MS` (url=419ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-142MS` (url=297ms, status=HTTP 204)
15. `AKUN-018-HOSTINGER-VLESS-WS-124MS` (url=248ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-180MS` (url=371ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-183MS` (url=418ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-201MS` (url=379ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-198MS` (url=401ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-230MS` (url=743ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-327MS` (url=614ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-371MS` (url=2238ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-480MS` (url=974ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-670MS` (url=968ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-UNKNOWN-VLESS-WS-93MS` (url=228ms, nekobox=252ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-109MS` (url=253ms, nekobox=218ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-117MS`
4. `AKUN-003-EU-VLESS-WS-91MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS`
6. `AKUN-006-UNKNOWN-VLESS-WS-124MS` (url=284ms, nekobox=232ms, status=no)
7. `AKUN-005-1PASSWORD-VLESS-WS-123MS`
8. `AKUN-006-008500-VLESS-WS-127MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-130MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-119MS`
11. `AKUN-009-MYBB-VLESS-WS-128MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-96MS` (url=214ms, nekobox=223ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-114MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-153MS` (url=278ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-131MS` (url=251ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-166MS` (url=249ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=257ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-386MS` (url=793ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-155MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-440MS` (url=915ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-140MS` (url=319ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-425MS` (url=763ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-421MS` (url=916ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-434MS` (url=833ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

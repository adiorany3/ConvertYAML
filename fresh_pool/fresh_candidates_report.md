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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-102MS` (url=281ms, nekobox=250ms, status=no)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-109MS` (url=287ms, nekobox=247ms, status=no)
3. `AKUN-001-CLOUDWEBMANAGE-EU-FR-VLESS-WS-101MS`
4. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-119MS` (url=278ms, nekobox=220ms, status=no)
6. `AKUN-003-UNKNOWN-VLESS-WS-123MS`
7. `AKUN-004-UNKNOWN-VLESS-WS-128MS`
8. `AKUN-005-MYBB-VLESS-WS-120MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-132MS`
10. `AKUN-010-DEV-VLESS-WS-124MS` (url=264ms, nekobox=228ms, status=no)
11. `AKUN-007-UNKNOWN-VLESS-WS-132MS`
12. `AKUN-008-UNKNOWN-VLESS-WS-135MS`
13. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-139MS`
14. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-147MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-110MS` (url=250ms, status=HTTP 204)
16. `AKUN-016-1PASSWORD-VLESS-WS-120MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-123MS` (url=311ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-143MS` (url=271ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-137MS` (url=294ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-104MS` (url=262ms, status=HTTP 204)
21. `AKUN-021-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-184MS` (url=296ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-330MS` (url=731ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-350MS` (url=694ms, status=HTTP 204)
24. `AKUN-024-CALMLOUD-VLESS-WS-365MS` (url=2325ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-379MS` (url=777ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

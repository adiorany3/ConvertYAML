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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=231ms, nekobox=186ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=211ms, nekobox=257ms, status=yes)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-66MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS`
10. `AKUN-009-COMPREND-NET-VLESS-WS-87MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=262ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-91MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-94MS` (url=194ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-129MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-155MS` (url=195ms, status=HTTP 204)
17. `AKUN-017-1PASSWORD-VLESS-WS-72MS` (url=198ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-139MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-140MS` (url=234ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-345MS` (url=799ms, status=HTTP 204)
21. `AKUN-021-MICROSOFT-VLESS-WS-385MS` (url=882ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-371MS` (url=779ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-370MS` (url=622ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-396MS` (url=841ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-412MS` (url=827ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

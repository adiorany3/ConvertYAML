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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=285ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=209ms, nekobox=249ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-84MS` (url=216ms, nekobox=234ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-76MS` (url=209ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=215ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=288ms, nekobox=235ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-97MS` (url=228ms, nekobox=253ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-107MS` (url=216ms, nekobox=239ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-92MS` (url=227ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-110MS` (url=232ms, nekobox=242ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-75MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-68MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-114MS` (url=196ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-87MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-87MS` (url=206ms, status=HTTP 204)
19. `AKUN-019-PAGES-VLESS-WS-85MS` (url=201ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-131MS` (url=210ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-244MS` (url=495ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-254MS` (url=555ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-254MS` (url=543ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-231MS` (url=498ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-258MS` (url=548ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

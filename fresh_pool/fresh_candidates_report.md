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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=199ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-57MS` (url=199ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=198ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=223ms, nekobox=229ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-79MS` (url=210ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-81MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-110MS`
11. `AKUN-012-DE-CLOUDKLEYER-20190515-VLESS-WS-142MS` (url=214ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-65MS` (url=199ms, status=HTTP 204)
13. `AKUN-014-FASTVPSUS-IPV4-VLESS-WS-148MS` (url=216ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-123MS` (url=324ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-100MS` (url=215ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-59MS` (url=212ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-65MS` (url=209ms, status=HTTP 204)
18. `AKUN-022-SUKARIO-VLESS-WS-388MS` (url=643ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-438MS` (url=729ms, status=HTTP 204)
20. `AKUN-024-UNKNOWN-VLESS-WS-390MS` (url=650ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-408MS` (url=681ms, status=HTTP 204)
22. `AKUN-028-UNKNOWN-VLESS-WS-211MS` (url=475ms, status=HTTP 204)
23. `AKUN-029-AS199785-DE-IPV4-VLESS-WS-500MS` (url=845ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-500MS` (url=844ms, status=HTTP 204)
25. `AKUN-031-AS199785-DE-IPV4-VLESS-WS-501MS` (url=839ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

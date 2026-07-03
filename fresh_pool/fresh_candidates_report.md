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
1. `AKUN-001-UNKNOWN-VLESS-WS-83MS` (url=212ms, nekobox=261ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS` (url=208ms, nekobox=232ms, status=yes)
3. `AKUN-003-ALIBABA-VLESS-WS-103MS` (url=232ms, nekobox=232ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-101MS` (url=233ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-108MS` (url=224ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-118MS` (url=220ms, nekobox=275ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-127MS` (url=228ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS` (url=223ms, nekobox=252ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-117MS` (url=199ms, nekobox=245ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-132MS` (url=219ms, nekobox=249ms, status=yes)
11. `AKUN-011-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-130MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-114MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-143MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-102MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-166MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-104MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-238MS` (url=498ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-240MS` (url=501ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-259MS` (url=544ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-273MS` (url=509ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-271MS` (url=555ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-272MS` (url=553ms, status=HTTP 204)
23. `AKUN-024-MICROSOFT-VLESS-WS-272MS` (url=589ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-422MS` (url=717ms, status=HTTP 204)
25. `AKUN-030-QURAN-VLESS-WS-456MS` (url=778ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

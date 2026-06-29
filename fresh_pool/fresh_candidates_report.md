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
1. `AKUN-001-UK-GB-DCL-01-20191003-VLESS-WS-62MS` (url=225ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-65MS` (url=226ms, nekobox=253ms, status=yes)
3. `AKUN-003-090227-VLESS-WS-63MS` (url=209ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=211ms, nekobox=240ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS` (url=210ms, nekobox=230ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-67MS` (url=328ms, nekobox=246ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=210ms, nekobox=242ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-108MS` (url=205ms, nekobox=176ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS`
10. `AKUN-009-ZVC-VLESS-WS-64MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-140MS` (url=325ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-122MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-116MS` (url=199ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-106MS` (url=196ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-101MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-107MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-342MS` (url=759ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-342MS` (url=714ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-389MS` (url=831ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-376MS` (url=656ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-399MS` (url=834ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-347MS` (url=729ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-414MS` (url=853ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-415MS` (url=868ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.

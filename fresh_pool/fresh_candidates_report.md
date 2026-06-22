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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-91MS` (url=273ms, nekobox=289ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-109MS` (url=219ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-108MS` (url=218ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=233ms, nekobox=263ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-105MS` (url=238ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=229ms, nekobox=247ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=199ms, nekobox=241ms, status=yes)
8. `AKUN-008-GO-DADDY-COM-LLC-VLESS-WS-133MS` (url=206ms, nekobox=252ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS` (url=288ms, nekobox=241ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-110MS` (url=216ms, nekobox=245ms, status=yes)
11. `AKUN-011-DEV-VLESS-WS-127MS` (url=244ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-269MS` (url=551ms, status=HTTP 204)
13. `AKUN-014-CONFLU-VLESS-WS-268MS` (url=539ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-274MS` (url=601ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-274MS` (url=546ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-286MS` (url=551ms, status=HTTP 204)
17. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-291MS` (url=580ms, status=HTTP 204)
18. `AKUN-019-WPENG-VLESS-WS-283MS` (url=580ms, status=HTTP 204)
19. `AKUN-022-KAWAII520-VLESS-WS-435MS` (url=682ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-478MS` (url=707ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-498MS` (url=833ms, status=HTTP 204)
22. `AKUN-028-SOLTANKABOS-VLESS-WS-569MS` (url=1005ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-640MS` (url=959ms, status=HTTP 204)
24. `AKUN-032-UK-GB-DCL-01-20191003-VLESS-WS-774MS` (url=1077ms, status=HTTP 204)
25. `AKUN-033-CLOUDFLARE-VLESS-WS-791MS` (url=1803ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
